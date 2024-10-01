


npm init
npm install express --save



mutation {
  addBook (name: "shiv", genre:"s", authorId:"66fbfc45cf86e1366954f01a") {
    name
    genre
  }
}


mutation {
  addAuthor (name: "shiv", age:34) {
    name
    age
  }
}

{
  book(id: "66fbfca3cf86e1366954f01e"){
    name
    id
    author {
      id
    }
	}
}

{
  books {
    name
    id
    author {
      id
    }
	}
}