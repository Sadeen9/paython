import logging
logging.basicConfig(level=logging.INFO)

with open("grades.txt","w") as f:
    f.write("Ali, A\n")
    logging.info("Saved grades for Ali")