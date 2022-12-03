import React, { useState, useContext } from "react";
import { ApiContext } from "../context/ApiContext";
import Modal from "react-modal";

const Ask = ({ask, prof}) => {
    Modal.setAppElement('#root')
    const { changeApprovalRequest, sendDMCont } = useContext(ApiContext);
    const [modalIsOpen, setModalIsOpen] = useState(false)
    const [text, setText] = useState('')

    const handleInputChange = () => (event) => {
        const value = event.target.value;
        setText(value);
    };
    const sendDM = () => {
        const uploadDM = new FormData();
        uploadDM.append("receiver", ask.askFrom);
        uploadDM.append("message", text);
        sendDMCont(uploadDM);
        setModalIsOpen(false);
    };
    const changeApproval = () => {
        const uploadDataAsk = new FormData();
        uploadDataAsk.append("askTo", ask.askTo);
        uploadDataAsk.append("approved", true);
        changeApprovalRequest(uploadDataAsk, ask);
    };


    return (
        <div>
            <h4> {prof[0].nickName}</h4>
            {!ask.approved ? (
                <button
                onClick={() => changeApproval()}
                >
                Approve
                </button>
            ) : (
                <button onClick={() => setModalIsOpen(true)}>
                send
                </button>
            )}

            <Modal
                isOpen={modalIsOpen}
                onRequestClose={() => setModalIsOpen(false)}
            >
                <div>Message</div>
                <input
                onChange={handleInputChange()}
                />
                <br />
                <button onClick={() => sendDM()}>
                sendDM
                </button>
                <button onClick={() => setModalIsOpen(false)}>
                close
                </button>
            </Modal>
        </div>
    )
}

export default Ask
