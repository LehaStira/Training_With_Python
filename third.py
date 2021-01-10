import json

def to_json(func):
    def wrapped(*args, **kwargs):
        data = json.dumps(*args, **kwargs)
        return func(data)
    return wrapped


@to_json
def logging(my_dict):
    with open('log.txt', 'w') as f:
        f.write(str(my_dict))


def main():
    my_dict = {'key': 'value'}
    logging(my_dict)

if __name__ == '__main__':
    main()