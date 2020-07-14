# for Tencent Cloud Function Service 

from daka.submit import main

def handle(event, context):
    main()

if __name__ == "__main__":
    handle(None, None)
