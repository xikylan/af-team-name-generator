import React, {useState} from "react";
import {Container, Row, Col} from "@appfolio/react-gears";

const PunDisplay = (puns) => {
    const [elements, setElements] = useState([]);

    const test = () => {
        let tempElements = [];

        console.log("test() puns: " );
        console.log(puns);

        for(let i = 0; i <= puns.length / 4; i++){
            tempElements.push(<Row>
                <Col xs={1}>{puns[i * 4]}</Col>
                <Col xs={1}>{puns[(i * 4) + 1]}</Col>
                <Col xs={1}>{puns[(i * 4) + 2]}</Col>
                <Col xs={1}>{puns[(i * 4) + 3]}</Col>
            </Row>)
        }

        if(tempElements.length > 0)
            setElements(tempElements);
    };

    // test();
    console.log(elements)

    return(
      <div>
          {/*<Container>*/}
          {/*    {elements}*/}
          {/*</Container>*/}
          {/*{puns}*/}
      </div>
    );
};

export default PunDisplay;