from pars import parse, save_to_file
if __name__ == "__main__":
    description = parse() 
    save_to_file(description, 'faculties.txt') 
    parse()
