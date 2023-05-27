import json,csv
def trainJson(tpath,rpath):
    with open(tpath) as file:data = json.load(file)
    questions,answers = [],[]
    for paragraph in data['data'][0]['paragraphs']:
        for qa in paragraph['qas']:question = qa['question'];answer = qa['answers'][0]['text'];questions.append(question);answers.append(answer)
    with open(rpath, 'w', newline='') as file:writer = csv.writer(file);writer.writerow(['Question', 'Answer']);writer.writerows(zip(questions, answers))
    print("Extraction completed and saved to data.csv")
def trainList(questions, answers, output_file="data.csv"):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file);writer.writerow(['Question', 'Answer'])
        for question, answer in zip(questions, answers): writer.writerow([question, answer])