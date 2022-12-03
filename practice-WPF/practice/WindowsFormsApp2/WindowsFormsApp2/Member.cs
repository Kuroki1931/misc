using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp2
{
    public abstract class Member
    {
        protected abstract float Rate { get; }
        public abstract string GetName();
        public float GetRate()
        {
            if (DateTime.Now.Day == 5)
            {
                return 0.5f;
            }
            if (DateTime.Now.Day == 30)
            {
                return 0.5f;
            }
            return Rate;
        }
    }

    public sealed class SilverMenber : Member
    {
        protected override float Rate => 1.0f;

        public override string GetName()
        {
            return "シルバー";
        }
    }

    public sealed class GoldMenber : Member
    {
        protected override float Rate => 0.8f;

        public override string GetName()
        {
            return "ゴールド";
        }
    }

    public sealed class PlatinumMenber : Member
    {
        protected override float Rate => 0.6f;

        public override string GetName()
        {
            return "プラチナ";
        }
    }
}
