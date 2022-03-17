import React, { useState } from "react";
import axios from "axios";
import logo from "./logo.svg";
import "./App.css";

function App() {
  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [id, setID] = useState("");
  const [user, setUser] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username && password) {
      const user = { username, password };
      console.log(user);
      setUser((user) => {
        return user;
      });
      setUserName("");
      setPassword("");
    } else {
      console.log("empty values");
    }
  };

  // new line start
  const [profileData, setProfileData] = useState(null);

  function getData() {
    axios({
      method: "GET",
      url: "/home/"+id,
    })
      .then((response) => {
        const res = response.data;
        setProfileData({
          profile_name: res.username,
          about_me: res.password,
        });
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  }
  function postData() {
    var bodyFormData = new FormData();
    bodyFormData.append("username", username);
    bodyFormData.append("password", password);
    axios({
      method: "post",
      url: "/form",
      data: bodyFormData,
      headers: { "Content-Type": "multipart/form-data" },
    })
      .then(function (response) {
        //handle success
        console.log(response);
      })
      .catch(function (response) {
        //handle error
        console.log(response);
      });
  }
  //end of new line
  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <div><h1>POST!</h1>
        <label>
          <p>Username: </p> 
          <input type="text" id='username' name='username' value={username} onChange={(e)=>setUserName(e.target.value)}></input>
        </label>
        <label>
        <p>Password: </p>
          <input type="password" id='password' name='password' value={password} onChange={(e)=>setPassword(e.target.value)}></input>
        </label>
        <br></br>
        <button type="submit" onClick={postData}>Submit</button>
        </div><br></br>
      </form>
      <h1>GET!</h1>
      <p>returns user with corresponding id</p>
      <input type='number' id='id' name='id' value={id} onChange={(e)=>setID(e.target.value)}></input>
      <button onClick={getData}>CLICK ME</button>
      {profileData && (
        <div>
          <p>Profile name: {profileData.profile_name}</p>
          <p>About me: {profileData.about_me}</p>
        </div>
      )}
    </div>
  );
}

export default App;
