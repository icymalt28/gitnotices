import React from "react"

function Card(props){
    return(

          <div className="term">
            <dt>
              <span className="emoji" role="img" aria-label="">
                {props.emoji}
              </span>
              <span>{props.name}</span>
            </dt>
            <dd>
              {props.meaning}
            <p> {props.body} </p>
            </dd>
          </div>


    )
}
 export default Card;

        
    
