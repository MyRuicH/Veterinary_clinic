def add_review(reviews: list) -> list:
    review = input("Залиште тут ваш відгук\n-> ")
    reviews.append(review)

    return reviews


def find_repeated_chars(reviews: list) -> None:
    reviewss = " ".join(reviews)
    repeated_groups = set()

    for i in range(len(reviewss)):
        for j in range(i + 1, len(reviewss)):
            slicce = reviewss[i:j]
            if reviewss.count(slicce) >= 2:
                repeated_groups.add(slicce)

    print(f"Список груп слів, які повторюються не менше 2 разів:\n-> {repeated_groups}")
