import React, { useState, useContext } from 'react'
import Modal from "react-modal";
import { ApiContext}  from "../context/ApiContext";

const Window = () => {
  Modal.setAppElement('#root')
  const { editedMemo, setEditedMemo, setCover, modalIsOpen, setModalIsOpen, editMemo } = useContext(ApiContext);
  const handleInputChange = () => (event) => {
    const value = event.target.value;
    const name = event.target.name;
    setEditedMemo({ ...editedMemo, [name]: value });
  };

  return (
    <div>
      
      <button onClick={() => setModalIsOpen(true)}
              style={{ marginLeft: '80%',
                       marginTop: '10px',
                       background: 'transparent',
                       border: 'none',
                    }}>
        Edit
      </button>
      <Modal isOpen={modalIsOpen} onRequestClose={()=> setModalIsOpen(false)}>
        <p>Title</p>
        <input type='text' value={editedMemo.title} name='title' onChange={handleInputChange()}/>
        <p>Picture</p>
        <input
            type="file"
            id="imageInput"
            onChange={(event) => {
                setCover(event.target.files[0]);
                event.target.value = "";
            }}
        />
        <p>Memo</p>
        <textarea name="memo" value={editedMemo.memo} cols="80" rows="50" wrap="hard" onChange={handleInputChange()}/>
        {editedMemo.title && editedMemo.memo ? (
          <button onClick={() => editMemo()}>
            ReCreate
          </button>
        ) : (
          <button disabled>
            ReCreate
          </button>
        )}
      </Modal>
    </div>
  )
}

export default Window
