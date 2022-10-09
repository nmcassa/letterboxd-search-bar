from letterboxdpy import user, movie, list
def build_prints() -> dict:
	return {"title": ["\n1. Search for User: ", 
						"2. Search for Movie: ",
						"3. Exit\n"],
			"user": ["\n1. User's favorite movies",
						"2. User's stats", #watchlist, stats
						"3. User's connections", 
						"4. User's watched movies", 
						"5. User's reviews",
						"6. Exit\n"], 
			"movie": ["\n1. Movie's rating",
						"2. Movie's details", #details director genre
						"3. Movie's popular reviews",
						"4. Exit\n"]}

def build_main(prints: list) -> str:
	for item in prints:
		print(item)
	return input()

def user_handler(prints: list):
	try:
		x = user.User(input("\nInput Username: ").lower())
	except:
		print("No User Found")
		exit()
	print("User Found")

	possible = ["1", "2", "3", "4", "5", "6"]
	
	while True:
		choice = "nothin"
		while choice not in possible:
			for item in prints:
				print(item)
			choice = input()

		print()

		if choice == "1":
			print("%s's Favorites:\n" % (x.username))
			for item in x.favorites:
				print(item[0])
		elif choice == "2":
			print("%s's Stats:\n" % (x.username))
			print("Watchlist: %s" % (x.watchlist_length))
			for k, v in x.stats.items():
				print("%s: %s" % (k, v))
		elif choice == "3":
			print("%s's Followers:\n" % (x.username))
			for item in user.user_followers(x):
				print(item)
			print("\n%s's Following:\n" % (x.username))
			for item in user.user_following(x):
				print(item)
		elif choice == "4":
			print("%s's Watched Films:\n" % (x.username))
			for item in user.user_films_watched(x):
				print(item[0])
		elif choice == "5":
			print("%s's Reviews:\n" % (x.username))
			for item in user.user_reviews(x):
				print("%s\n %s\t\t %s\n %s" % (item["movie"], item["date"], item["rating"], item["review"]))
		else:
			exit()
		
		option = input("\nWould you like more info about this user? (Y/N)")
		if option == "N" or option == "n":
			exit()

def movie_handler(prints: list):
	try:
		x = movie.Movie(input("\nInput Movie Title: ").lower())
	except:
		print("No Movie Found")
		exit()
	print("Movie Found")

	possible = ["1", "2", "3", "4"]
	
	while True:
		choice = "nothin"
		while choice not in possible:
			for item in prints:
				print(item)
			choice = input()

		print()

		if choice == "1":
			print("%s's rating: %s" % (x.title.replace("-", " "), x.rating))
		elif choice == "2":
			for k, v in movie.movie_details(x).items():
				print(k + ": ")
				for item in v:
					print(item)
				print()
			try:
				print("Director:\n" + x.director)
			except:
				print("Directors:\n" + x.directors)
			print("\nGenres:")
			for item in x.genres:
				print(item)
		elif choice == "3":
			for item in movie.movie_popular_reviews(x):
				print()
				print("%s\n %s\n %s" % (item["reviewer"], item["rating"], item["review"]))
		else:
			exit()

		option = input("\nWould you like more info about this movie? (Y/N)")
		if option == "N" or option == "n":
			exit()

if __name__ == "__main__":
	choice = "0"

	prints = build_prints()

	while choice != "1" and choice != "2" and choice != "3":
		if choice == "3":
			exit()
		choice = build_main(prints["title"])

	if choice == "1":
		user_handler(prints["user"])
	elif choice == "2":
		movie_handler(prints["movie"])
	else:
		exit()


