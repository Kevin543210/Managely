import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import '../Styles/LoginStyles.css'
import axios from "axios";

function Login() {

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post("/login", {
        email,
        password,
      });
      if (response.data.success) {
        window.location.href = "/Home";
      } else {
        setMessage("Invalid email or password");
      }
    } catch (error) {
      console.error(error);
    }
  };



  return (
    <div>
      <div className='Logintitle'>
        Managely
      </div>
      <form className='Logincontainer' onSubmit={handleSubmit}>
          <input
            placeholder='email'
            className='Loginitem'
            type="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
        <br />
          <input
            placeholder='password'
            className='Loginitem'
            type="password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
        <br />
        {message && <p className='message'>{message}</p>}
        <button className='LoginsubmitButton' type="submit">Submit</button>
        <a className='LoginforgotP' href='/'>
          Forgot Password?
        </a>
      </form>
      
    </div>
  )
}

export default Login