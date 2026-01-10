import { useEffect, useState } from "react";
import api from "../api";

function Articles() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    api.get("articles/")
      .then(res => setArticles(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Articles</h1>
      {articles.map(a => (
        <div key={a.id}>
          <h3>{a.title}</h3>
          <p>{a.content}</p>
        </div>
      ))}
    </div>
  );
}

export default Articles;
