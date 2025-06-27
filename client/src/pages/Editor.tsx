import Files from "../components/File"
import "../styles/editor.css"

const Editor =()=>{
    return(
        <div
        className="page"
        >
            <Files/>
        <textarea 
        name="" 
        id=""
        ></textarea>
        </div>
    )
}

export default Editor