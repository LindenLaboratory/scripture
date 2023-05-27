import json,csv
def trainJson(tpath, rpath):
    with open(tpath) as file: data = json.load(file)
    questions, answers = [], []
    for section in data['data']:
        title = section['title']
        for paragraph in section['paragraphs']:
            for qa in paragraph['qas']:
                question = qa['question']
                if qa['answers']: answer = qa['answers'][0]['text']
                else:answer = ""
                questions.append(question);answers.append(answer)
    with open(rpath, 'w', newline='', encoding='utf-8') as file: writer = csv.writer(file);writer.writerow(['Question', 'Answer']);writer.writerows(zip(questions, answers))
    print("Extraction completed and saved to", rpath)
def trainList(questions, answers, output_file="data.csv"):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file);writer.writerow(['Question', 'Answer'])
        for question, answer in zip(questions, answers): writer.writerow([question, answer])
trainJson("data.json","data.csv")
