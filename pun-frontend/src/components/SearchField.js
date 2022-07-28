import React, {useState} from "react";
import {Button, Col, Container, ListGroup, Row} from "@appfolio/react-gears";
import {List} from "@appfolio/react-gears";
import PunDisplay from "./PunDisplay";

const SearchField = () => {
    const [name, setName] = useState();
    const [puns, setPuns] = useState();
    const [elements, setElements] = useState([]);

    const test = (data) => {
        let tempElements = [];

        console.log("test() puns: " );
        console.log(puns);

        for(let i = 0; i <= data.length / 4; i++){
            tempElements.push(<Row>
                <Col xs={1}>{data[i * 4]}</Col>
                <Col xs={1}>{data[(i * 4) + 1]}</Col>
                <Col xs={1}>{data[(i * 4) + 2]}</Col>
                <Col xs={1}>{data[(i * 4) + 3]}</Col>
            </Row>)
        }

        if(tempElements.length > 0)
            setElements(tempElements);
    };


    const getResults = () => {
        const url = `/generate/non_recursive?input=${name}`;
        console.log("HERE");

        fetch(url).then((response) => {
            return response.json();
        }).then( (data) => {
            setPuns(data);
            // test(data);
        }).catch( () => console.log("error"));
    };

    return(
        <div className={"title"}>
            <form>
                <label>
                    <input type="text" name="name" className={'custom-search'} onChange={(event) => setName(event.target.value)}/>
                </label>
            </form>
            <Button onClick={getResults}>Get Results</Button>
            <List
                height={'70vh'}
                items={puns}
                striped={false}
                flush={false}
                >
                {(item) => <h1>{item}</h1>}
            </List>
        </div>
    )
};

export default SearchField;