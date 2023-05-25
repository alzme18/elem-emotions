import argparse
from scripts.train import train
from scripts.predict import predict

def main():
    parser = argparse.ArgumentParser(description="ElemEmotion: Emotion Analysis AI")
    parser.add_argument('--mode', type=str, required=True, help='Mode: "train" or "predict"')
    parser.add_argument('--text', type=str, help='Text to predict emotion for (required if mode is "predict")')
    args = parser.parse_args()

    if args.mode == "train":
        train()
    elif args.mode == "predict":
        if args.text is None:
            print('You must provide text when using "predict" mode')
        else:
            print(predict(args.text))
    else:
        print('Invalid mode. Choose either "train" or "predict".')

if __name__ == "__main__":
    main()
