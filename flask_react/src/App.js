import React, { useState } from "react";
import axios from "axios";
import logo from "./logo.svg";
import "./App.css";

function App() {
  //set up useStates for variables used
  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [id, setID] = useState("");
  
  //used on post submit
  const handleSubmit = (e) => {
    //prevents submitting default text
    e.preventDefault();
    //if username and password not ''
    if (username && password) {
      //console log the user object because i wanna know NOW
      const user = { username, password };
      console.log(user);
      //reset back to default values
      setUserName("");
      setPassword("");
    } else {
      //return error if neither filled out in console
      console.log("empty values");
    }
  };

  //POLL VOTING SCRIPT//
  const [vote, setVote] = useState("");
  const [results, setResults] = useState("");

  const handleSubmitPoll = (e) => {
    e.preventDefault();
    if (vote) {
      console.log(vote);
      setVote("");
    } else {
      console.log("empty values");
    }
  };

  function postPollData(e) {
    e.preventDefault();
    var bodyPollData = new FormData();
    bodyPollData.append("vote", vote);
    axios({
      method: "POST",
      url: "/voteForm",
      data: bodyPollData,
      headers: { "Content-Type": "multipart/form-data" },
    })
      .then(function (response) {
        //handle success
        getPollData()
        console.log(response);
      })
      .catch(function (response) {
        //handle error
        console.log(response);
      });
  }

  function getPollData() {
    axios({
      method: "GET",
      url: "/voteGet",
    })
      .then((response) => {
        //set response data to res
        const res = response.data;
        var finalResults=""
        Object.entries(res).forEach(([key, value]) => {
          finalResults=finalResults + key+' : '+value + ' votes <br>'
        });
        setResults({
          //set values to correct values
          finalResults
        });
        console.log(results)
      })
      //error catching
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
        }
      });
  }
  //END OF POLL SCRIPT//

  //set up usestate for profiledata
  const [profileData, setProfileData] = useState(null);
  //get method
  function getData() {
    axios({
      method: "GET",
      url: "/home/" + id,
    })
      .then((response) => {
        //set response data to res
        const res = response.data;
        setProfileData({
          //set values to correct values
          profile_name: res.username,
          password: res.password,
        });
      })
      //error catching
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
        }
      });
  }
  //post method
  function postData() {
    var bodyFormData = new FormData();
    bodyFormData.append("username", username);
    bodyFormData.append("password", password);
    axios({
      method: "POST",
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
  //RETURN STATEMENT
  return (
    <div className="App">
      <form onSubmit={handleSubmitPoll}>
        <div>
          <h1>VOTE HERE!</h1>
          <label>
            <h2>Cast your vote!: </h2>
            <input
              type="text"
              id="vote"
              name="vote"
              value={vote}
              onChange={(e) => setVote(e.target.value)}
            ></input>
            <button type="submit" onClick={postPollData}>
              Submit Vote
            </button>
          </label>
        </div>
      </form>
      <h1>GET VOTES!</h1>
      <h2>Results of votes</h2>
      <h3><div dangerouslySetInnerHTML={{__html:results.finalResults}}></div></h3>
            {/* end of poll data */}



      <form onSubmit={handleSubmit}>
        <div>
          <h1>POST!</h1>
          <label>
            <p>Username: </p>
            <input
              type="text"
              id="username"
              name="username"
              value={username}
              onChange={(e) => setUserName(e.target.value)}
            ></input>
          </label>
          <label>
            <p>Password: </p>
            <input
              type="password"
              id="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            ></input>
          </label>
          <br></br>
          <button type="submit" onClick={postData}>
            Submit
          </button>
        </div>
        <br></br>
      </form>
      <h1>GET!</h1>
      <p>returns user with corresponding id</p>
      <input
        type="number"
        id="id"
        name="id"
        value={id}
        onChange={(e) => setID(e.target.value)}
      ></input>
      <button onClick={getData}>CLICK ME</button>
      {profileData && (
        <div>
          <p>Profile name: {profileData.profile_name}</p>
          <p>About me: {profileData.password}</p>
        </div>
      )}
    </div>
  );
}

export default App;
