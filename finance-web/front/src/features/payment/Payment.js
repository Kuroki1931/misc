import React, {useState} from "react";
import classes from './Payment.module.css'
import {CardElement, useElements, useStripe} from "@stripe/react-stripe-js";
import ApiService from "./api";
import Button from '@material-ui/core/Button';

const Payment = () => {
    const [error, setError] = useState(null);
    const [email, setEmail] = useState('');
    const stripe = useStripe();
    const elements = useElements();

    const handleChange = (event) => {
        if (event.error) {
          setError(event.error.message);
        } else {
          setError(null);
        }
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        const card = elements.getElement(CardElement);
 
        const {paymentMethod, error} = await stripe.createPaymentMethod({
            type: 'card',
            card: card
        });
        ApiService.saveStripeInfo({
            email: email, payment_method_id: paymentMethod.id})
          .then(response => {
            console.log(response.data);
          }).catch(error => {
            console.log(error)
        })
        
    };


    return (
        <div className={classes.all}>
            <div className={classes.head}>
                決済
            </div>
            <form onSubmit={handleSubmit} className={classes.form_all}>
                <div className={classes.email_all}>
                    <div htmlFor="email">Email Address</div>
                    <input className={classes.email_input} id="email" name="name" type="email" 
                     placeholder="jenny.rosen@example.com" required 
                     value={email} onChange={(event) => { setEmail(event.target.value)}} 
                    />
                </div>
                <div className={classes.credit_all}>
                    <label for="card-element">Credit or debit card</label> 
                    <CardElement id="card-element" onChange={handleChange} className={classes.card}/>
                    <div className="card-errors" role="alert">{error}</div>
                </div>
                <div className={classes.button_all}>
                    <Button type="submit" className="submit-btn" variant="contained" color="primary">
                        Submit Payment
                    </Button>
                </div>
            </form>
        </div>
    )
}

export default Payment
