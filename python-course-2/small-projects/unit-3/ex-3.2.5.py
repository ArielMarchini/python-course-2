
def read_file(file_name):
    file = None
    try:
        file = open(file_name, 'r')
        return "__CONTENT_START__\n" + "".join(file.readlines()) + "\n__CONTENT_END__"
    except:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"""
    finally:
        if file is not None:
            file.close()


print(read_file("heytxt"))