import colorama, argparse, os, time

""" Crete py file by template """


def get_args():
    """create args"""
    parser = argparse.ArgumentParser(
        description="!TODO", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("filepath", metavar="str", help="get file path")
    parser.add_argument(
        "template_name",
        metavar="str",
        default="default",
        help="get template name or try to create new",
    )

    return parser.parse_args()


def author_data():
    #!TODO вынести этот ужас в файл с константами
    return f"""# file created: {time.ctime()}
# by Dmustache`s  tool
# email: dvusakov@gmail.com
# Github: https://Github.com/DMustache\n\n
"""


def format_template_name(template_name):
    return f"templates/" + template_name + ".py"


def create_template(filepath, template_name):
    """create template by filepath"""
    with open(
        format_template_name(template_name), mode="w", encoding="utf-8"
    ) as to_write:
        with open(filepath, mode="r", encoding="utf-8") as to_read:
            to_write.write(to_read.read())


def create_file(filepath, template_name):
    """create file by template in templates directory"""
    with open(filepath, mode="w", encoding="utf-8") as to_write:
        with open(template_name, mode="r", encoding="utf-8") as to_read:
            lst = to_read.readlines()
            if "import" in lst[0]:
                lst.insert(1, author_data())
            else:
                lst.insert(0, author_data())

        to_write.writelines(lst)


def main():
    """Jazz here"""
    args = get_args()
    path_arg = args.filepath
    template_name_arg = args.template_name
    template = format_template_name(template_name_arg)

    #!TODO проверка наличия файла на месте, где пользователь хочет создать новый файла
    #!TODO проверка наличия темплейта, если нету, запросить создвать новый на основе существуещего файла
    #!TODO проверка на существование темплейта, если пользователь хочет создать новый темплейт

    create_file(path_arg, template)


if __name__ == "__main__":
    main()
