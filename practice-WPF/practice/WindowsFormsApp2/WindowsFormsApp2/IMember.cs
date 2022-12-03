using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp2
{
    public interface IMember
    {
        float Rate { get; }
        string GetName();
    }

    //public sealed class SilverMenber: IMember
    //{
    //    public float Rate => 1.0f;

    //    public string GetName()
    //    {
    //        return "シルバー";
    //    }
    //}

    //public sealed class GoldMenber : IMember
    //{
    //    public float Rate => 0.8f;
    //    public string GetName()
    //    {
    //        return "ゴールド";
    //    }
    //}

    //public sealed class PlatinumMenber : IMember
    //{
    //    public float Rate => 0.6f;
    //    public string GetName()
    //    {
    //        return "プラチナ";
    //    }
    //}
}
