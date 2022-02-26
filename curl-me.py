import sys, getopt
import requests
import json
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer as timer

# Call the right amount of requests - total requests against number of workers
def correct_requests(range_count, workers):
    return round(range_count/workers)

# Function that makes the request
def make_requests(range_count, url, payload, headers, request_count):
    start= timer()
    # TO-DOs:
    ## Add logic so we can use also use POST / PUT / Other http methods for the calls rather than just GET
    ## Add logic to better handle the responses for better visibility
    for count in range(range_count):
        respone = requests.get(url,data=payload,headers=headers)
        print(respone)
        request_count += 1
    print('Called', request_count,'many times. It took', timer() - start,'long!')

# Main function to retrieve user input then call the request function
def main(argv):

    # Initialize variables
    url, payload, headers, method, request_count, range_count, workers= '', '', '', '', 1, 10, 3

    # Get values from user input
    try:
        opts, args = getopt.getopt(argv,'hu:r:p:g:',['help=','url=', 'range=', 'payload=','headers=', 'method=' ])
    except getopt.GetoptError as err:
        # Print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        print('python3 curl-me.py -u <api> -p <payload> -h <headers> -r <range_count>')
        sys.exit(2)

    for opt, arg in opts:
        # TO-DO: Add a -h, --help for help menu
        if opt in ('-h', '--help'):
            print(arg)
            sys.exit('curl-me.py -u <api> -p <payload> -h <headers> -r <range_count>')
        elif opt in ('-u', '--url'):
            # TO-DO: Add use cases to verify that URL added is indeed a proper
            url= arg if arg != ''  else sys.exit('Please enter an API URL')
            # print(url)
        elif opt in ('-r', '--range'):
            if(arg.isnumeric()):
                range_count= int(arg)
            else:
                sys.exit('Please enter a numeric value greater than 0')
        elif opt in ('-p', '--payload'):
            payload= json.dumps(arg) # Necessary to pass a JSON object payload, errors out otherwise
        elif opt in ('--headers'):
            headers= json.dumps(arg)
        elif opt in ('-m', '--method'):
            method= arg.lower()

    range_count = correct_requests(range_count, workers)

    with ThreadPoolExecutor(max_workers=workers) as executor:
        for worker in range(workers):
            future = executor.submit(lambda p: make_requests(*p), (range_count, url, payload, headers, request_count))

if __name__ == "__main__":
   main(sys.argv[1:])
