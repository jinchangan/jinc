from pandas import pd


def print_colorful_text(text, color):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }

    if color in colors:
        colored_text = colors[color] + text + colors['reset']
        print(colored_text)
    else:
        print(text)


def update_sql(sql_link,sql_name: str, set_args: dict, where_param: dict):
    if isinstance(sql_name, str) and isinstance(set_args, dict) and isinstance(where_param, dict):
        # 处理数据的逻辑
        pass
        # 在这里进行你的具体操作
    else:
        print_colorful_text("输入的参数类型错误。", "red")
    cursor = sql_link.cursor()
    set_ = ""
    for k, v in set_args.items():
        set_ += k + " = " + str(v) + ","
    set_ = set_.strip(",")
    where_param_ = ""
    for k, v in where_param.items():
        where_param_ += f" {k}={str(v)} and "
    where_param_ = where_param_.strip().strip("and")
    delete_sql = f"update {sql_name} set {set_} where {where_param_};"
    print_colorful_text(delete_sql, "green")
    cursor.execute(delete_sql)
    cursor.close()
    sql_link.commit()


def set_sql(engine,sql_name, **args):
    keya = []
    vala = []
    for k, v in args.items():
        print(k, v)
        keya.append(f"{k}")
        vala.append(v)

    f2 = pd.DataFrame(columns=keya)
    s2 = pd.Series(
        vala,
        index=keya)
    f2 = f2.append(s2, ignore_index=True)
    f2.to_sql(name=sql_name, con=engine, if_exists='append', index=False, index_label=False)