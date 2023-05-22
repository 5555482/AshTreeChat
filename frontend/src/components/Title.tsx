import { useState } from 'react';
import axios from "axios";

type Props = {
    setMessages: any;
}


function Title({ setMessages }: Props) {
    const [isResetting, setIsResetting] = useState(false);

    const resetConversation = async () => {
        setIsResetting(true);
        await axios.get("http://localhost:8000/reset").then((res) => {
            if (res.status == 200) {
                setMessages([])
            } else {
                console.error("There was an error with the API request")
            }
        }).catch((err) => console.error(err.message));
        setIsResetting(false);
    }

    return (
        <div onClick={resetConversation} className='bg-indigo-500 p-5'><button>RESET</button></div>
    )
}

export default Title