# encoding = utf-8
import yaml


def load(file: str = "questions.yaml") -> list:
    """
    Load all questions dict from the named file.
    :param file: The name of the yaml file, default to "questions.yaml".
    :return: A list consisting all the required data.
    """
    try:
        with open(file, "r", encoding="utf-8") as records:
            questions = yaml.load(records, Loader=yaml.FullLoader)
            return questions
    except FileNotFoundError:
        print("文件：", file, "不存在！", sep="")


def dump(file: str = "questions.yaml") -> None:
    """
    Ask for question id and question title from command line, and write them to the named file.
    :param file: The name of the yaml file, default to "questions.yaml"
    :return: None
    """
    questions = []
    print("按\"q\"随时返回上级")
    while True:
        question_id = input("知乎问题id：")
        if question_id == "q":
            break
        try:
            question_id = int(question_id)
        except ValueError:
            print("知乎问题id必须为正整数，请重新输入！")
            continue

        question_title = input("问题名字：")
        if question_title == "q":
            break
        questions.append({"question_id": question_id, "question_title": question_title})
        print()

    try:
        with open(file, "a", encoding="utf-8") as records:
            records.write(yaml.dump(questions))
            print("您的输入已经被保存至：", file, sep="")
    except FileNotFoundError:
        print("文件：", file, "无法被写入！", sep="")


if __name__ == "__main__":
    print("yaml相关操作")
    while True:
        choice = input("写入新数据请按1，查看所有数据请按2，退出请按0：")
        if choice == "1":
            file = input("写入文件名，使用默认文件名请只按回车：")
            if file == "":
                dump()
            else:
                dump(file)

        elif choice == "2":
            file = input("读取文件名，使用默认文件名请只按回车：")
            if file == "":
                print(load())
            else:
                print(load(file))

        elif choice == "0":
            break

        else:
            print("无此选项：", choice, sep="")

        print()
