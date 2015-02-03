import crawler
import creator

def main():
	if crawler.main():
		creator.main()
	else:
		print('A problem has occured while getting data from bilkent.edu.tr')


if __name__ == "__main__":
    main()

