def simplifyPath(path):
    path_list = [p for p in path.split("/") if p != "." and p != ""]
    # print(path_list)
    final = []
    for i in path_list:
        if i == "..":
            if final:
                final.pop()
        else:
            final.append(i)
    final_string = "/" + "/".join(final)
    # print(final_string)
    return final_string

    