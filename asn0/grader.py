from zipfile import ZipFile
import os
import shutil
import subprocess
import xlsxwriter


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

    return ''


def find_readme(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            if "read" in f.lower() and '._' not in f.lower():
                return os.path.join(root, f)

    return ''


def extract_and_grade(necessary_files):
    sections = [os.path.join(os.getcwd(), "submissions", dir) for dir in os.listdir(
        os.path.join(os.curdir, "submissions")) if "CSC" in dir]
    workbook = xlsxwriter.Workbook(
        'grades.xlsx')

    section_num = 0

    for section_dir in sections:
        # section_number = section_dir[section_dir.find(
        #     "6650")+4:section_dir.find("-")]
        section_num += 1
        worksheet = workbook.add_worksheet("section-" + str(section_num))
        worksheet.set_default_row(20)
        
        row = 0

        student_dirs = [os.path.join(section_dir, d) for d in os.listdir(
            section_dir) if "assignsubmission" in d]

        for path in student_dirs:
            # path = os.path.join(os.curdir, dire)
            if(not os.path.isdir(path)):
                continue

            files = [f for f in os.listdir(path)]
            found_zip = False
            student_name = path.split("/")[-1].split('_')[0].replace(' ', '-')

            for f in files:
                file_path = os.path.join(path, f)
                f_ext = f.split('.')

                if f_ext[len(f_ext) - 1] != 'zip' and f_ext[len(f_ext) - 1] != 'rar':
                    continue

                if f_ext[len(f_ext) - 1] == 'rar':
                    found_zip = True
                    subprocess.call(["unar", file_path, "-o", path, "-f"])

                elif f_ext[len(f_ext) - 1] == 'zip':
                    with ZipFile(file_path, 'r') as zip:
                        found_zip = True
                        zip.extractall(path)

                grading_files = []
                missing_files = []

                readme_loc = find_readme(path)
                readme_redir = os.path.join(
                    os.getcwd(), "README", student_name)
                os.makedirs(readme_redir, exist_ok=True)

                if readme_loc:
                    shutil.copy(readme_loc, readme_redir)
                else:
                    missing_files.append("README")

                print("finding files...")
                path_to_moss_submission = os.path.join(
                    os.getcwd(), "moss", "submissions", student_name)
                os.makedirs(path_to_moss_submission, exist_ok=True)

                for f in necessary_files:
                    p = find(f, path)
                    if p == '':
                        missing_files.append(f)
                    else:
                        grading_files.append(p)
                        shutil.copy(p, path_to_moss_submission)

                if(len(grading_files) == len(necessary_files)):
                    graded = grade(grading_files,
                                   student_name, os.path.join(section_dir, "../subgrader"))
                    worksheet.write(row, 0, student_name)
                    if graded == '':
                        worksheet.write(
                            row, 1, 'Error encountered while grading.')
                    else:
                        worksheet.write(row, 1, graded[0])
                        worksheet.write(row, 2, graded[1])
                        worksheet.write(row, 3, graded[2])

                    row += 1
                else:
                    worksheet.write(row, 0, student_name)
                    worksheet.write(
                        row, 1, 'Missing these files: '+str(missing_files))
                    row += 1

            if not found_zip:
                worksheet.write(row, 0, path[2:].split('_')[0])
                worksheet.write(
                    row, 1, "Did not submit .zip or .rar file format")
                row += 1
    workbook.close()


def grade(locations_of_files, name, subgrader_path):
    new_file_locations = []
    for floc in locations_of_files:
        shutil.copy(floc, subgrader_path)
        new_file_locations.append(os.path.join(subgrader_path,os.path.basename(floc)))

    # change this if not using conda
    print("Grading " + name + "...\n")
    try:
        score = subprocess.run('python autograder.py', shell=True,
                               cwd=subgrader_path, stdout=subprocess.PIPE, timeout=60*3).stdout.decode('utf-8')
    except subprocess.TimeoutExpired:
        return ('Timeout occured after 3 minutes', '', '')
    except Exception as e:
        return('Error: ' + e, '', '')

    for floc in new_file_locations:
        os.unlink(floc)

    return (score[score.find('Total:')+6:score.find('Your grades')], score[score.find('Provisional grades'):score.find('Your grades')], score)


if __name__ == "__main__":
    extract_and_grade(['addition.py', 'buyLotsOfFruit.py', 'shopSmart.py'])
    print("==============================================\ndone!\n==============================================")
    