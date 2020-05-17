# encoding = utf-8
import yaml


def load(file="records.yaml"):
    """
    :param file: The name of the yaml file, default to "records.yaml".
    :return: A list consisting all the required data.
    """
    with open(file, "r") as records:
        questions = yaml.load(records, Loader = yaml.FullLoader)
    return questions


def dump(file="records.yaml"):
    """
    :param file: The name of the yaml file, default to "records.yaml"
    :return: None
    """
    questions = []
    while True:
        print("按\"q\"退出")
        question_id = input("知乎问题id：")
        if question_id == "q":
            break
        question_id = int(question_id)
        question_title = input("问题名字：")
        questions.append({"question_id": question_id, "question_title": question_title})
    with open(file, "w") as records:
        records.write(yaml.dump(questions))


if __name__ == "__main__":
    dump()
