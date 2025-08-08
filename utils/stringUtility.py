class stringUtility:
    def indent_string(string, indent=4):
        """
        Indents a string by a specified number of spaces.
        Args:
            string (str): The string to indent.
            indent (int): The number of spaces to indent the string.
        Returns:
            str: The indented string.
        """
        return ' ' * indent + string
    
    def split_string(string, max_length=50):
        """
        Splits a string into lines of a specified maximum length.
        If the string is shorter than max_length, it returns the string as a single line.
        The function ensures that words are not split in the middle.
        If a word is longer than max_length, it will be split into multiple lines.
        Args:
            string (str): The string to split.
            max_length (int): The maximum length of each line.
        Returns:
            list: A list of strings, each no longer than max_length.
        """
        if len(string) <= max_length:
            return [string]
        
        words = string.split()
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line) + len(word) + 1 <= max_length:
                if current_line:
                    current_line += " "
                current_line += word
            else:
                lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines
    
    
    def add_pipes(string):
        """Adds a pipe character at the end of each line.
        Args:
            string (str): The string to add pipes to.
        Returns:
            str: The string with pipes added at the start and end."""
        return ("|" +string+"|")
    

    def add_spaces(string, length=50):
        """Adds spaces to a string to ensure it has a specified length.
        Args:
            string (str): The string to add spaces to.
            length (int): The desired length of the string.
        Returns:
            str: The string padded with spaces to the specified length.
            """
        return string.ljust(length)
    
    def add_space_at_end(string, length=50):
        """Adds spaces to the end of a string to ensure it has a specified length.
        Args:
            string (str): The string to add spaces to.
            length (int): The desired length of the string.
        Returns:
            str: The string padded with spaces to the specified length.
            """
        return string.rjust(length, ' ')
    
    def add_space_to_center(string, length=50):
        """Adds spaces to the end of a string to ensure it has a specified length.
        Args:
            string (str): The string to add spaces to.
            length (int): The desired length of the string.
        Returns:
            str: The string padded with spaces to the specified length, centered.
            
        """
        return string.center(length, ' ')
    
    def piped_separator(separator="-", length=50):
        """Returns a separator line with pipes. it will be 2 characters longer than the length parameter due to the add of pipes
        Args:
            separator (str): The character to use for the separator. Default is "-".
            length (int): The length of the separator line.
        Returns:
            str: The separator line with pipes at the start and end.
        """
        return "|" + separator * (length) + "|"


    def format_string(string, length=50, indent=2, dedent=2, join=True, Just=0):
        """
        Formats a string to fit within a specified length, with indentation and dedentation.
        note that the string wil be 2 character longer than the length parameter due to the add of pipes
        Args:
            string (str): The string to format.
            length (int): The maximum length of each line.
            indent (int): The number of spaces to indent each line. (default is 2)
            dedent (int): The number of spaces to remove from the start of each line. (default is 2)
            join (bool): If True, joins the lines with newlines. If False, returns a list of lines.
            Just (int): Justification type: 0 for left, 1 for right, 2 for center. (default is 0)
        Returns:
            str: The formatted string with lines split, indented, and piped.
        """
        lines = stringUtility.split_string(string, length-(indent+dedent))
        for i in range(len(lines)):
            lines[i] = stringUtility.indent_string(lines[i], indent)
            if Just == 0 :
                lines[i] = stringUtility.add_spaces(lines[i], length)
            elif Just == 1 :
                lines[i] = stringUtility.add_space_at_end(lines[i], length)
            elif Just == 2 :
                lines[i] = stringUtility.add_space_to_center(lines[i], length)

            lines[i] = stringUtility.add_pipes(lines[i])
        return '\n'.join(lines) if join else lines



#print (stringUtility.format_string("Example string to demonstrate the utility function.  This will be split into multiple lines if it exceeds the specified length.",50,2,8,0))  # Example usage of the utility function