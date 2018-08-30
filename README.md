# Springer_abstract_scrapper

Script written in python that retrieves the abstract of HTML pages of SpringerLink.

What Springer does not offer:
-> bibtex (only CSV)
tip: open it in a spreadsheet editor e copy the DOI column. Paste it into Zotero which will create the bibtex for you. However, Zotero does not retrieve the abstract, so you have to use the script in the following way:

1. in both "with open('search_Springer.bib')" change to your bibtex file name;
2. run the script;

At the end the script will overwrite the original bibtex file with a version with abstracts entries. If you get your IP blocked the script will stop but will keep the job done befone the error, just run again.
