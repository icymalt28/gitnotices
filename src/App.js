import React from "react"
import Card from "./Card"
import emojipedia from "./emojipedia";

function Create(emojiterm){
  return(
        <Card 
        name={emojiterm.name}
       
        meaning={emojiterm.meaning}
        
        body={emojiterm.body}

        />
  )

}



function App() {
  return ( 
          <div>
        <h1>
          <span>GIT notice board</span>
        </h1>
  
        <dl className="dictionary">
          {emojipedia.map(Create)}
        </dl>

  </div>


  );
}

export default App;
