# a util for file read and write
import os
import json


def json_output(in_struct, path=None):
    if path is not None:
        data_to_write = {}
        if os.path.exists(path):
            with open(path, "r") as f_exist:
                file = f_exist.read()
                if len(file) > 0:
                    data_to_write = json.loads(file)
                else:
                    data_to_write = {}
            data_to_write.update(in_struct)
            f_exist.close()
        else:
            with open(path, "w") as f_new:
                f_new.write("")
            data_to_write.update(in_struct)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data_to_write, f, indent=None)
            f.close()
    else:
        print(json.dumps(in_struct, default=str))


def json_read(uuid: str, champ: str):
    path = "./data/credentials/" + uuid

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        f.close()

    return data[champ]
