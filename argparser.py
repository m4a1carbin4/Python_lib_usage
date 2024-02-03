#argparse 활용한 파라미터 인자값 처리 로직 연습

from argparse import ArgumentParser

def main(): 
    parser = ArgumentParser()

    parser.add_argument("--data_input",type=str,default="testing_default",help="study")
    
    args = parser.parse_args()
    
    print(args.data_input)

if __name__ == "__main__" :
    main()