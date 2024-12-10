class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        
        self._name = name
        self._articles = []  # List to hold articles authored by the author

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        # Return unique magazines using set to ensure no duplicates
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        # Use a set to ensure unique topic areas
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        
        self._name = name
        self._category = category
        self._articles = []  # List to hold articles published in the magazine

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        return self._articles

    def contributors(self):
        # Return unique authors who have contributed to the magazine
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        # Ensure we return a list of article titles as strings
        return [article.title for article in self._articles]

    def contributing_authors(self):
        # Create a dictionary to count the number of articles by each author
        author_article_count = {}
        for article in self._articles:
            author_article_count[article.author] = author_article_count.get(article.author, 0) + 1
        # Filter authors who have written more than 2 articles
        return [author for author, count in author_article_count.items() if count > 2]


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self._author = author
        self._magazine = magazine
        self._title = title

        # Add this article to both the author's and magazine's respective collections
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        self._magazine = new_magazine
