"""
Functions to handle all files related actions
"""

import csv
import json
import xml.etree.ElementTree as ET


def load_data_json(file_name):
    """
    function to load the file and create a JSON file
    """
    try:
        with open(file_name, 'r') as data, open('./saved/final_students.json', 'w') as json_file:
            lines = []
            for line in data:
                final_data = {}
                data = line.split(',')
                for item in data:
                    key, separator, value = item.partition(':')
                    final_data[key.strip()] = value.strip()
                lines.append(final_data)
            json.dump(lines, json_file, indent=4)
    except FileNotFoundError as error:
        print(error)
    else:
        print('JSON file has been successfully created')


def load_data_csv(file_name):
    """
    function to load the file and create a CSV file
    """
    header = ['id', 'firstname', 'lastname', 'password']
    try:
        with open(file_name, 'r') as data, open('./saved/final_students.csv', 'w') as csv_file:
            csv_data = csv.reader(data)
            csv_line = csv.writer(csv_file)
            csv_line.writerow(header)

            for line in csv_data:
                line = [item.replace(r + ':', '')
                        for item, r in zip(line, header)]
                csv_line.writerow(line)
    except FileNotFoundError as error:
        print(error)
    finally:
        print('CSV file has been successfully created')


def load_data_xml(file_name):
    """
    function to load the file and create a XML file
    """
    lines = []
    student_config = ET.Element('students')
    try:
        with open(file_name, 'r') as data:
            student_config = ET.SubElement(student_config, 'students')
            for line in data:
                lines = line.strip().replace('\n', '')
                student = ET.SubElement(student_config, 'student')
                for item in range(len(lines.split(','))):
                    items = lines.split(',')[item].split(':')
                    result = ET.SubElement(student, items[0])
                    result.text = items[1]

                tree = ET.ElementTree(student_config)
                tree.write('./saved/final_students.xml',
                           encoding='utf-8', xml_declaration=True)
    except FileNotFoundError as error:
        print(error)
    else:
        print('XML file has been successfully created')
