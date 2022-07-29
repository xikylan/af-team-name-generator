import React from "react";
import Title from "./Title";
import SearchField from "./SearchField";
import Footer from "./Footer";

const HomeScreen = () => {
    return(
        <div className={"HomeScreen"} >
            <Title/>
            <SearchField/>
            <Footer/>
        </div>
    )
};

export default HomeScreen;