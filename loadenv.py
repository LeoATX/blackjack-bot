class Env:
    def __init__(self):
        self.env_dictionary = dict()

        # This handles the error of file not found
        try:
            env_file = open('.env')
        except FileNotFoundError:
            print("no .env file")
            return

        for line in env_file.readlines():
            # First clean up the line
            line = line.strip()
            line = line.strip('\n')

            # The line is empty
            if len(line) == 0:
                continue

            # Splits the line into a list of two objects
            line = line.split('=')

            # Clean up after split
            line[0] = line[0].strip()
            line[1] = line[1].strip()
            # This strips the "
            line[1] = line[1].strip('\"')

            self.env_dictionary[line[0]] = line[1]

    def getenv(self, key): # noqa
        try:
            return self.env_dictionary[key]
        except KeyError:
            # Return none when the key is not found
            return None
