from student import Student

def main():

	a = Student("Elle")
	b = Student("Brian")

	# No scores added yet
	a.avg_score()

	a.add_score(80)
	a.add_score(95)
	a.add_score(85)

	a.avg_score()

	b.add_score(85)
	b.add_score(100)
	b.add_score(85)

	b.avg_score()


if __name__ == "__main__":
	main()

