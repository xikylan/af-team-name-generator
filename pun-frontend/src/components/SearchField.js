import React, {useState} from "react";
import {Button} from "@appfolio/react-gears";
import {List} from "@appfolio/react-gears";
import {Input, Form} from "@appfolio/react-gears";

const SearchField = () => {
    const [name, setName] = useState();
    const [puns, setPuns] = useState();

    const getResults = () => {
        const url = `/generate/non_recursive?input=${name}`;

        fetch(url).then((response) => {
            return response.json();
        }).then( (data) => {
            setPuns(data);
        }).catch( () => console.log("error"));
    };

    const onSubmit = (event) => {
        console.log("HERE")
        event.preventDefault();
        getResults();
    };

    const styling = {
        "margin-top": '10px',
        "margin-bottom": '30px'
    };

    return(
        <div className={"title"}>

            <Form onSubmit={onSubmit}>
                <Input placeholder="Enter Original Name: " id="hello"
                       onSubmit={onSubmit}
                       onChange={(event) => setName(event.target.value)}

                />
            </Form>

            <Button onClick={getResults} block color={"primary"} style={styling}>Generate Names</Button>

            <List
                height={'20vh'}
                items={puns}
                striped={true}
                flush={false}
                >
                {(item) =>
                    <h5>
                        {item}
                    </h5>
                }
            </List>
        </div>
    )
};

export default SearchField;