import React from "react";

const SearchField = () => {
    return(
        <div className={"title"}>
            <form>
                <label>
                    Enter: {' '}
                    <input type="text" name="name" className={'custom-search'}/>
                </label>
            </form>
        </div>
    )
};

export default SearchField;