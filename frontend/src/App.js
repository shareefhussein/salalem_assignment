import React, { Component } from 'react';

class App extends Component {
  state = {
    Artists: [],
    Albums: [],
    Songs: []
  };

  async componentDidMount() {
    try {
      const res1 = await fetch('http://127.0.0.1:8000/artists/api');
      const Artists = await res1.json();

      const res2 = await fetch('http://127.0.0.1:8000/albums/api');
      const Albums = await res2.json();

      const res3 = await fetch('http://127.0.0.1:8000/songs/api');
      const Songs = await res3.json();

      this.setState({
        Artists, Albums, Songs

      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        
        <h1>List of Artists</h1>
        {this.state.Artists.map(item => (
          <div key={item.id}>
            <h2>{item.first_name} {item.last_name} </h2>
          </div>
        ))}

        <h1>List of Albums</h1>
        {this.state.Albums.map(item2 => (
          <div key={item2.id}>
            <h2>{item2.album_title} {item2.last_name} </h2>
          </div>
        ))}

        <h1>List of Songs</h1>
        {this.state.Songs.map(item3 => (
          <div key={item3.id}>
            <h2>{item3.song_title} {item3.last_name} </h2>
          </div>
        ))}
      </div>
    );
  }
}

export default App;






