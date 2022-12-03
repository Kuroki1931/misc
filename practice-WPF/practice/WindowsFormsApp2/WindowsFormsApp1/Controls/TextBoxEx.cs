using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public sealed class TextBoxEx : TextBox
    {
        protected override void OnLeave(EventArgs e)
        {
            int value = 0;
            if(!int.TryParse(this.Text, out value))
            {
                this.Text = "0";
            }

            base.OnLeave(e);
        }
    }
}
