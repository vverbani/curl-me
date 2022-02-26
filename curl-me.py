import sys, getopt
import requests
import json

# Main function to hit your endpoint(s) X times
def main(argv):

    # Initialize variables
    url= ''
    range_count= 10
    payload= ''
    headers= ''
    method= ''

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
            # TO-DO: Add use cases to verify that URL added is indeed a proper URL
            url= arg if arg != ''  else sys.exit('Please enter an API URL')
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

    # TO-DOs:
    ## Add multi threads to highten the load amount per second
    ## Add logic so we can use also use POST / PUT / Other http methods for the calls rather than just GET
    ## Add logic to better handle the responses for better visibility
    for x in range(range_count):
        respone = requests.get(url,data=payload,headers=headers)
        print(respone)
        print(x + 1)

if __name__ == "__main__":
   main(sys.argv[1:])
