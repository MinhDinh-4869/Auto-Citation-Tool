import subprocess
import re

AUTHOR_PLACEHOLDER = '[[[AUTHORS]]]'
PUBLICATION_DATE_PLACEHOLDER = '[[[PUBLICATION DATE]]]'
TITLE_PLACEHOLDER = '[[[TITLE]]]'

class CitationMaker:
    def __init__(self, src="", des=""):
        self.src = src
        self.des = des

    def make_citation(self):
        try:
            subprocess.call(["autocite", "--from-file", f"{self.src}", "--to-text", f"{self.des}", "--non-interactive", "--format", "apa"])
        except Exception as e:
            print(f"Error when trying to make citation: {e}")
    
    def post_process(self):
        filehandle = open(self.des, "r", encoding="utf-8")
        lines = filehandle.readlines()
        filehandle.close()

        filehandle = open(self.des, "w", encoding="utf-8")
        idx = 1
        for line in lines:
            if line not in ["", "\n"]:
                processed_line = self.process_line(line=line)
                filehandle.write(f"{idx}.\t{processed_line}")
                idx+=1
        
        filehandle.close()

    def process_line(self, line=""):
        line = line.replace(TITLE_PLACEHOLDER, self.make_sub_title(line))
        line = line.replace(PUBLICATION_DATE_PLACEHOLDER, "n.d.")
        line = line.replace(AUTHOR_PLACEHOLDER, self.make_sub_author(line))
        return line

    def make_sub_author(self, line="") -> str:
        url = re.search("https://.*", line)
        if url != None:
            items = url.group().split("/")
            return items[2]
        return ""

    def make_sub_title(self, line="") -> str:
        url = re.search("https://.*", line)
        if url != None:
            items = url.group().split("/")
            #items = items[2:] #remove https://
            if items[-1] in [""]:
                return items[-2].upper().replace("-", " ").replace(".HTML", "")
            return items[-1].upper().replace("-", " ").replace(".HTML", "")
        return ""