import { useEffect, useState } from "react";
import api from "../api";

function Videos() {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    api.get("videos/")
      .then(res => setVideos(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Videos</h1>
      {videos.map(v => (
        <div key={v.id}>
          <h3>{v.title}</h3>
        </div>
      ))}
    </div>
  );
}

export default Videos;
